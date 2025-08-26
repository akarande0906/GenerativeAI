# A Basic MCP Server implementation 

Experimenting with the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) to create an MCP Server.

Refer to [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/getting-started/intro) here.


**Pre-requisites**

1. Install the [uv package manager](https://docs.astral.sh/uv/). 
2. Install [Visual Studio Code](https://code.visualstudio.com/) (Note: This will work with Claude as well. More details on how to run MCP Servers in Claude are provided in the MCP documentation link above).

**Setup**

1. Navigate to the project directory and set up the UV environment:
   
```
uv sync
```

2. Start the virtual environment:

```
source .venv/bin/activate

```

Alternately, open the Command Palette ( using CMD+SHIFT+P on MAC or CTRL+P on Windows and select 'Python: Set project environment' and select the 'activate' binary.

3. Install dependant libraries:
```
uv pip install <package-name>
```
   
4. Test the MCP Server in Dev Mode:
   
```
uv run dev server.py
```

**Running the MCP Server**


*Pre-requisite:* Ensure that your version of Visual Studio code supports MCP Server (v1.102 or later)

1. Open the Command Palette.
2. Select 'MCP: Open User Configuration'. This opens mcp.json. This file configures MCP Servers in the current workspace. 
3. Add the following json here:
   ```
    {
        "servers": {
            "```
            basic_mcp_server
            ```": {
            "type": "stdio",
            "command": "uv",
            "args": [
                "run",
                "--directory",
                "/absolute/path/to/basic_mcp_server",
                "mcp-open-meteo"
            ]
        }
    },
    "inputs": []
    }

   ```

4. Click on the 'Start' button to run the MCP Server. Alternately from the Command Palett, click on 'MCP: List Servers' to manage the MCP Server.


   
**Working with the MCP Server**

This MCP Server is very basic (hence the name) and supports the following functionality:

1. Add 2 numbers
2. Generate a Greeting for the user.
3. Gets the weather for a specific city.
4. Tells you a 'Dad' joke.

To interact with the MCP Server, in the Chat interface set the mode to 'Agent' instead of 'Ask'.

**TBD**

I am adding more features to the MCP Server. Generally MCP Servers cater to a specific domain/feature, but I'm going to call this a Swiss Army Knife just to experiment with different interfaces. What I'm planning to add/update next:
1. The Simple weather service will pick up the first matching city name. So 'Whats the weather in Salem' for example may return the weather for Salem, Oregon and not Salem, Massachusetts. This ambiguity can be addressed through elicitation, which needs to be added in. 
2. The code in server.py is packed into one file. This will need to be modularized for better readability.
3. Write MCP Servers for very specific domains.
