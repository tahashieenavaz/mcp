# Advanced MCP Concepts

### Sampling

Sampling is a technique where the MCP server asks the MCP client to run a language model prompt on its behalf. Instead of the server directly calling the language model (like Claude), it sends a request to the client, which then makes the call and returns the generated text to the server. This approach shifts the complexity and responsibility of calling the language model from the server to the client. It’s especially useful for publicly accessible MCP servers because it avoids the server needing an API key or paying for token usage, enhancing security and cost control. Essentially, sampling lets the server delegate text generation to the client, simplifying server operations.

### (Directory) Roots

A root is a designated file or folder that a user grants the server permission to access. Think of roots as security boundaries: the server can only read files and folders within these roots. This setup helps the server know where it’s allowed to look for files, so users don’t have to provide full file paths every time. It also ensures the server can’t access files outside those specified areas, enhancing security and control. Essentially, roots let the MCP server focus on specific parts of your file system safely and conveniently.
