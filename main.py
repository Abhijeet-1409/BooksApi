from typing import Dict, Optional
from fastapi import Body, FastAPI , HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from model import Book
from info import books
from enum import Enum

app = FastAPI()

original_openapi = app.openapi

def  custom_openApi() :
    
    if app.openapi_schema :
        return app.openapi_schema
    
    modified_openapi_schema = original_openapi()

    if "components" in modified_openapi_schema :
        components = modified_openapi_schema["components"]
        if "schemas" in components :
            schemas = components["schemas"]
            if "Book" in schemas :
                book_schema = schemas["Book"] 
                if "properties" in book_schema :
                    book_schema["properties"].pop("id",None)

    if "paths" in modified_openapi_schema :
        paths = modified_openapi_schema["paths"]
        if "/books/{bookId}" in paths : 
            put_method = paths["/books/{bookId}"].get("put")
            if put_method and "requestBody" in put_method :
                request_body = put_method["requestBody"]
                if "content" in request_body :
                    content = request_body["content"]
                    if "application/json" in content:
                        schema = content["application/json"]["schema"]
                        if "type" in schema and schema["type"] == "object":
                            schema.pop("additionalProperties", None)
                            schema["additionalProperties"] = False

    app.openapi_schema = modified_openapi_schema
    return modified_openapi_schema


app.openapi = custom_openApi




@app.get("/books")
async def getAllBooks() :
    try :
        content = {"books":[ book.model_dump() for book in books]}
        return JSONResponse(content=content,status_code=200)
    except Exception as error: 
        print(error)
        raise HTTPException(detail="Internal Error",status_code=500)    


@app.post("/books")
async def createBook(book:Book) :
    try :
        content = {"message":f"book {book.book_title} is added with id {book.id}"}
        books.append(book)
        return JSONResponse(content=content,status_code=201) 
    except HTTPException as http_exc:
        raise http_exc     
    except Exception as error:
        print(error)
        raise HTTPException(detail="Internal Error", status_code=500)
    

@app.get("/books/{bookId}")
async def getBook(bookId : str) :
    try :
       book = next(filter(lambda b: b.id == bookId, books), None)
       if book is None  :
           raise HTTPException(detail=f"Book with id {bookId} did not found",status_code=404)
       content = book.model_dump_detail()
       return JSONResponse(content=content,status_code=200)
    except HTTPException as http_exc:
        raise http_exc     
    except Exception as error: 
        print(error)
        raise HTTPException(detail="Internal Error",status_code=500)



@app.put("/books/{bookId}") 
async def updateBook(bookId: str, request_body: Dict[str, Optional[str]] = Body(...)):
    try:
        book = next((b for b in books if b.id == bookId), None)
        if book is None:
            raise HTTPException(detail=f"Book with id {bookId} does not exist", status_code=404)
        
        book_data = book.model_dump_detail()
        
        del book_data["id"]
        
        for key, value in request_body.items():
            book_data[key] = value
      
        try:
            temp_book = Book(**book_data)
            del temp_book
        except ValidationError as e:
            response_body = {"detail":e.errors()}
            raise HTTPException(status_code=422, detail=response_body)

        for key, value in request_body.items():
            if value not in (None, ""): 
                setattr(book, key, value)

        content = {
            "message": f"Book with id {bookId} has been updated",
            "book": book.model_dump()
        }
        return JSONResponse(content=content, status_code=200)

    except HTTPException as http_exc:
        raise http_exc
    except Exception as error:
        print(error)
        raise HTTPException(detail="Internal Error", status_code=500)


@app.delete("/books/{bookId}")
async def deleteBook(bookId : str) :
    try :
        condition = lambda b : b.id == bookId
        book_index = next((i for i,value in enumerate(books) if condition(value)),None)
        if book_index is None:
            raise HTTPException(detail=f"book with id {bookId} did not found",status_code=404)
        del books[book_index]
        content = {
            "message" : f"book with id{bookId} has been deleted"
        }
        return JSONResponse(content=content,status_code=200)
    except HTTPException as http_exc:
        raise http_exc     
    except Exception as error:
        print(error)
        raise HTTPException(detail="Internal Error", status_code=500)

