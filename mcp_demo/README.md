# MCP Demo — Hello Tools & Resources

This repository demonstrates a simple **Model Context Protocol (MCP)** setup —  
a Python **server** exposing tools and resources, and a **client** that connects via STDIO.

---

## Overview

**Model Context Protocol (MCP)** lets models, tools, and local systems exchange structured context securely and consistently.  
This demo includes:

- A multi-tool MCP **server** (`say_hello`, `add_numbers`, `reverse_text`, `get_time`)
- Example **resources** (static + dynamic(can be added))
- A Python **client** using `stdio_client` to communicate with the server

---

## Project Structure
```
mcp_demo/
├── hello_client.py # MCP client
├── server/
│ ├── hello_server.py # MCP server
│ └── static/
│ └── greeting.md # Example Markdown resource (optional)
└── README.md
```

---

## Setup Instructions

### Prerequisites

- **Python 3.11+**
- (Optional) **uv** for running MCP servers quickly:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh

### Create and activate your environment
```python
# Create a new directory for our project
uv init mcp_demo
cd mcp_demo

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx

pip install uv
pip install --upgrade pip setuptools wheel
pip install fastapi uvicorn httpx rich typer

# Create our server file
touch hello_server.py

```


### Client start the server/client - Start manually
```python
uv run hello_server.py

- In another terminal
python hello_client.py
```

## Tools in the Server
| Tool           | Description              | Example Output                                      |
| -------------- | ------------------------ | --------------------------------------------------- |
| `say_hello`    | Greets the user          | `Hello, Smittal! 👋 Welcome to the Chewy MCP Demo.` |
| `add_numbers`  | Adds two numbers         | `12.0`                                              |
| `reverse_text` | Reverses a string        | `ywehC`                                             |
| `get_time`     | Returns current UTC time | `Current time in UTC: 2025-10-06 14:46:55 UTC`      |

## Resources in the Server
| URI                             | Type            | Example Content                                            |
| ------------------------------- | --------------- | ---------------------------------------------------------- |
| `resource://static/greeting.md` | Static Markdown | `# Welcome to the Chewy MCP Demo!`                         |
| `resource://chewy/info.txt`     | Dynamic text    | `Chewy MCP Server v1.0 – Serving happiness (and tools) 🐶` |



## Client output

```
[10/06/25 09:46:55] INFO     Processing request of type           server.py:664
                             ListToolsRequest                                  

Tools: ['say_hello', 'add_numbers', 'reverse_text', 'get_time']
                    INFO     Processing request of type           server.py:664
                             ListResourcesRequest                              

📚 Resources: [AnyUrl('resource://static/greeting.md')]
                    INFO     Processing request of type           server.py:664
                             CallToolRequest                                   

👋 say_hello → [TextContent(type='text', text='Hello, Smittal! 👋 Welcome to the Chewy MCP Demo.', annotations=None, meta=None)]
                    INFO     Processing request of type           server.py:664
                             CallToolRequest                                   
add_numbers → [TextContent(type='text', text='12.0', annotations=None, meta=None)]
                    INFO     Processing request of type           server.py:664
                             CallToolRequest                                   
reverse_text → [TextContent(type='text', text='ywehC', annotations=None, meta=None)]
                    INFO     Processing request of type           server.py:664
                             CallToolRequest                                   
get_time → [TextContent(type='text', text='Current time in UTC: 2025-10-06 14:46:55 UTC', annotations=None, meta=None)]
                    INFO     Processing request of type           server.py:664
                             ReadResourceRequest                               

📖 greeting.md →
# Welcome to the Chewy MCP Demo!\n\nThis is a sample resource.
(mcp_demo) smittal@XTYX4W42XY mcp_demo % 
```
