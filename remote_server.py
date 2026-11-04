from fastmcp import FastMCP

mcp = FastMCP('Amazon Exommerce')

@mcp.tool
def search_product():
    '''The Available products in amazon'''
    products = ['Mobile','laptops','Headphones','smartwatches','SmartBands']
    return products

@mcp.tool
def get_offers():
    '''This gives the offers on the products'''

    offers = {'mobile': '10%','laptp':'15%','Headphones':'12%'}
    return offers

@mcp.tool
def order_status():
    '''The order status of delivery'''

    return "The Product is delivered"

@mcp.tool
def payment():
    '''This tells whether payment is done or not'''

    status = 'yes'
    return status


if __name__ == '__main__':
    mcp.run(transport='streamable-http',port=5001,host='0.0.0.0')