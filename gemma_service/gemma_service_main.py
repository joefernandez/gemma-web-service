#
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from fastapi import FastAPI
from pydantic import BaseModel
from gemma_model import create_message_processor

app = FastAPI()
model_processor = create_message_processor() # initialize model

class Request(BaseModel):
    text: str

class Response(BaseModel):
    text: str

@app.post("/gemma_request/")
async def process_text(request: Request):
    """
    Processes the input text and returns a modified version.
    """
    # Your text processing logic here
    # response_text = request.text.upper()  # Example: Convert to uppercase

    response_text = model_processor(request.text)

    response = Response(text=response_text)
    return response

# TEST FUNCTION ONLY: DELETE
@app.get("/hello/")
async def root():
    return {"message": "Hello World"}


def get_prompt():
    return "You are an expert coder who is "