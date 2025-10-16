from fastapi import FastAPI
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
import os

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/query")
async def query_travel_agent(query: QueryRequest):

    try:
        print(f"Query received: {query}")
        graph = GraphBuilder()
        react_app = graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph PNG saved as my_graph.png in {os.getcwd()}")

        messages = {"messages": [query.question]}
        output = react_app.invoke(messages)

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Last AI response
        else:
            final_output = str(output)

        return {"answer": final_output}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})