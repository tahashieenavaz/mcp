from pydantic import Field
from mcp.server.fastmcp import FastMCP

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
    new_content: str = Field(
        description="The new content to be swapped with the old content of the document."
    ),
) -> None:
    if document_identifier not in docs:
        raise ValueError(f"Document {document_identifier} was not founded.")

    docs[document_identifier] = new_content


# TODO: Write a resource to return all doc id's

# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
