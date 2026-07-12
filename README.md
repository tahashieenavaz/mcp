# Model Context Protocol 

## Notes

Our server usually has a MCP client inside that communicates with a MCP server somewhere outside the server. 

**Transport Agnostic**: the communication between client and server can be done over many different protocols.
- Standard I/O
- HTTP
- WebSockets

The MCP [specification](https://modelcontextprotocol.io/specification) defines different types of messages that can be exchanged.

MCP Flow:
![](images/mcp-flow.png)

Normally a project will implement either a MCP server or a MCP client, not both.

<hr />

In order to test our MCP server we can use **MCP Inspector**. That could be loaded using:

```bash
mcp dev mcp_server_file.py
```

Then we will have browser access to an inspector for our MCP server.