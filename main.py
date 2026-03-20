from fastmcp import FastMCP 
import random 
import json 

mcp = FastMCP(name="Simple calculator Server") 

@mcp.tool
def add(a: int, b:int) -> int: 
    """Add two numbers together
    
    args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    
    """
    return a + b 

@mcp.tool 
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generate a random number between min_val and max_val
    
    args:
        min_val: The minimum value (default: 1)
        max_val: The maximum value (default: 100)

    Returns:
        A random integer between min_val and max_val
    """
    return random.randint(min_val, max_val) 

@mcp.resource("info://server") 
def server_info() -> str: 
    """ Get the server information""" 
    info = {
        "name": "Simple calculator Server",
        "version": "1.0.0",
        "description": "A basic mcp server with math tools",
        "tools": ["add", "random_number"],
        "auth": "Debdarshi" 
    } 
    return json.dumps(info, indent=2) 

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000) 
    
