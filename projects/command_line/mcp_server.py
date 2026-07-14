from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


@mcp.tool(
    name="read_document_content",
    description="Reads the contents of a document and returns it as a String.",
)
def read_document_content(
    document_identifier: str = Field(
        description="The identifier of a document to read"
    ),
) -> str:
    if document_identifier not in docs:
        raise ValueError(f"Document {document_identifier} does not exist.")

    return docs[document_identifier]


@mcp.tool(
    name="edit_document",
    description="Edits the contents of a document and raises a ValueError if the document has not been founded.",
)
def edit_document(
    document_identifier: str = Field(
        description="The identifier of the document to edit."
    ),
    old_content: str = Field("The old content that will be searched and replaced"),
    new_content: str = Field(
        description="The new content to be swapped with the old content of the document."
    ),
) -> None:
    if document_identifier not in docs:
        raise ValueError(f"Document {document_identifier} was not founded.")

    docs[document_identifier] = docs[document_identifier].replace(
        old_content, new_content
    )


@mcp.resource("docs://documents", mime_type="application/json")
def list_documents() -> list[str]:
    return list(docs.keys())


@mcp.resource("docs://documents/{document_id}", mime_type="text/plain")
def get_document(document_id: str) -> str:
    if document_id not in docs:
        raise ValueError(f"Document {document_id} does not exist.")
    return docs[document_id]


@mcp.prompt(name="format", description="Rewrite the contents of a document in Markdown")
def format_document_prompt(
    document_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document from any given format to Markdown.
    The ID of the document to reformat is:
    <document_id>
    {document_id}
    </document_id>

    Use all the tools at your disposal to finish the job.
    """

    return [base.UserMessage(prompt)]


# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
