from graphene_django.utils.testing import GraphQLTestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class AddToDoTestCase(GraphQLTestCase):
    def test_add_mutation(self):
        response = self.query(
            '''
            mutation AddToDoMutation($title: String!, $description: String!){
                AddToDoMutation(title: $title, description : $description) {
                    title
                    description
                }
            }
            ''',
            op_name='AddToDoMutation',
            variables={'title': 'Task 1', 'description': 'Task 1 description'}
        )


        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

class DeleteToDoTestCase(GraphQLTestCase):
    def test_valid_delete_player(self):
        response = self.delete(
                reverse('single_task', kwargs={'pk': self.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
