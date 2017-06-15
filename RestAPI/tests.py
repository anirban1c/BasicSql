from falcon import testing
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
import server


class MyTestCase(testing.TestCase):
	def setUp(self):
		super(MyTestCase, self).setUp()

		self.app = server.app


class TestRestUris(MyTestCase):
	def test_get_log1_resp(self):

		result = self.simulate_get('/log/log_sample_1.log')
		self.assertEquals(result.status_code, 200)

	def test_get_log1_data(self):

		result = self.simulate_get('/log/log_sample_1.log')
		self.assertGreater(len(result.json), 0)

	def test_get_log2(self):

		result = self.simulate_get('/log/log_sample_2.log')
		self.assertEquals(result.status_code, 200)

	def test_get_404(self):

		result = self.simulate_get('/log/log_sample_2333.log')
		self.assertEquals(result.status_code, 404)

