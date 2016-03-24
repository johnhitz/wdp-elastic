import eve
from eve_elastic import Elastic

app = eve.Eve(data=Elastic)
# app.config['CONFIG']

if __name__ == '__main__':
    app.run()