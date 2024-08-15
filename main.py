from fastapi import FastAPI , HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict
from info import names,authors
import json
app = FastAPI()

class Book(BaseModel) :
    name : str
    author : str




book_Dict : Dict[str,Book] = {
    f"{names[i]}": Book(name=names[i], author=authors[i])
    for i in range(len(names))
}


@app.get("/books")
async def getAllBooks() :
    try :
        content = {"books":{key:value.model_dump() for key,value in book_Dict.items()}}
        return JSONResponse(content=content,status_code=200)
    except Exception as error: 
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
        book_Dict[f"book-{book.name}"] = book
        content = {"message":f"book {book.name} is added with id {book.name}"}
        return JSONResponse(content=content,status_code=201) 
    except HTTPException as http_exc:
        raise http_exc     
    except Exception as error:
        print(error)
        raise HTTPException(detail="Internal Error", status_code=500)


@app.put("/books/{bookId}") 
async def updateBook(bookId : str) :
    pass

@app.delete("/books/{bookId}")
async def deleteBook(bookId : str) :
    pass

