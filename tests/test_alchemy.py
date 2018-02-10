
import nose
from nose.tools import *
import unittest2 as unittest


from My_Alchemy import Flight_Alch, Alchemy_Connection
from data_model import Flight, Connection


class AlchemyTest(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def teardownClass(cls):
    	pass

    def setUp(self):
    	pass

    def tearDown(self):
    	pass


    def test_insert_bulk(self):
        alchemy = Alchemy_Connection(path_to_file='sqlite:///memory:2')

        conn = Connection('LUZ', 'VNO')
        cc_flights =[]
        w = Flight('Airflot', '354', connection=conn,
              departureDateTime= '2018-10-11', currencyCode='RUB', basePrice='100', discountedPrice='68', 
              administrationFeePrice='30') 
        cc_flights.append(w)
        w1 = Flight(airLine='WIZZ', flightNumber='150', connection=conn,
              departureDateTime= '2020-10-11', currencyCode='USD', basePrice='150', discountedPrice='90', 
              administrationFeePrice='31') 
        cc_flights.append(w1)
        alchemy.insert_flights(cc_flights)

        flights_in_db = alchemy.get_all_flights()
        eq_(len(flights_in_db), 2)
        ok_(w in flights_in_db)
        ok_(w1 in flights_in_db)


