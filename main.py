from fastapi import FastAPI , HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict
from info import names,authors
import uuid

app = FastAPI()

class Book(BaseModel) :
    name : str
    author : str

    class Config :
        extra = "forbid"

class RequestModel(BaseModel) :
    class Config :
        extra = "allow"



def generateBookId() :
    return str(uuid.uuid4())


book_Dict : Dict[str,Book] = {
    f"book-{generateBookId()}": Book(name=names[i], author=authors[i])
    for i in range(len(names))
}


@app.get("/books")
async def getAllBooks() :
    try :
        content = {"books":{key:value.model_dump() for key,value in book_Dict.items()}}
        return JSONResponse(content=content,status_code=200)
    except Exception as error: 
        print(error)
        raise HTTPException(detail="Internal Error",status_code=500)    


@app.get("/books/{bookId}")
async def getBook(bookId : str) :
    try :
       if bookId not in book_Dict :
           raise HTTPException(detail=f"Book with id {bookId} did not found",status_code=404)
       content = book_Dict[bookId].model_dump()
       return JSONResponse(content=content,status_code=200)
    except HTTPException as http_exc:
        raise http_exc     
    except Exception as error: 
        print(error)
        raise HTTPException(detail="Internal Error",status_code=500)


@app.post("/books")
async def createBook(book:Book) :
    try :
        errors = []
        for key,value in book.model_dump().items() :
            if isinstance(value,str) and not value :
                errors.append(f"{key} value cannot be empty it is required")
        if len(errors):
            error_message = "; ".join(errors)
            raise HTTPException(detail=error_message, status_code=422)
        bookId = f"book-{generateBookId()}"
        book_Dict[bookId] = book
        content = {"message":f"book {book.name} is added with id {bookId}"}
        return JSONResponse(content=content,status_code=201) 
    except HTTPException as http_exc:
        raise http_exc     
    except Exception as error:
        print(error)
        raise HTTPException(detail="Internal Error", status_code=500)


@app.put("/books/{bookId}") 
async def updateBook(bookId : str,updatedBook : RequestModel) :
    try :
        invalid_fields = []
        requestBody = updatedBook.model_dump()
        if bookId not in book_Dict :
            raise HTTPException(detail=f"book with {bookId} did not exist",status_code=404)
        if "additionalProp1" in requestBody or len(requestBody.keys()) == 0 :
            raise HTTPException(detail=f"please enter fields",status_code=400)
        book = book_Dict[bookId]
        for key in requestBody.keys() :
            if not hasattr(book,key) :
               invalid_fields.append(f"{key} is not a valid field")
        if invalid_fields :
            detail = {
                "invalid fields" : invalid_fields,
            }
            raise HTTPException(detail=detail,status_code=400)

        for key,value in requestBody.items() :
            if hasattr(book,key) and value is str and value:
                setattr(book,key,value)
        content = {
            "message":f"book with id {bookId} has been updated",
            "book": book.model_dump()
        }
        return JSONResponse(content=content,status_code=200)
    except HTTPException as http_exc:
        raise http_exc     
    except Exception as error:
        print(error)
        raise HTTPException(detail="Internal Error", status_code=500)



@app.delete("/books/{bookId}")
async def deleteBook(bookId : str) :
    try :
        if bookId not in book_Dict :
            raise HTTPException(detail=f"book with id {bookId} did not found")
        del book_Dict[bookId]
        content = {
            "message" : f"book with id{bookId} has been deleted"
        }
        return JSONResponse(content=content,status_code=200)
    except HTTPException as http_exc:
        raise http_exc     
    except Exception as error:
        print(error)
        raise HTTPException(detail="Internal Error", status_code=500)

