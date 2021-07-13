from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

class SnackTest(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='qusa',
            password='qusai111',
        )
        self.snack=Snack.objects.create(
            name='Burger',
            description='delicious',
            purchaser=self.user,
        )

    def test_snack_status_code(self):
        self.assertEqual(200,self.client.get(reverse('snack_list')).status_code)   

    def test_string_representation(self):
        self.assertEqual(str(self.snack),'Burger')    


    def test_snack_list_view(self):
        actual=self.client.get(reverse('snack_list')) 
        self.assertEqual(actual.status_code,200)
        self.assertContains(actual,'Burger')
        self.assertTemplateUsed(actual,'snack_list.html')    


    def test_detail_view(self):
        response = self.client.get(reverse("snack_details", args="1"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Purchaser :qusai")
        self.assertTemplateUsed(response, "snack_detail.html")  

    def test_create_view(self):
        response = self.client.get(reverse("snack_details", args="1"))
        self.assertEqual(response.status_code, 200)

    def test_create_view_add(self):
        actual=self.client.post(reverse('snack_details',args='1'), {
            {'name':'chicken burger' , 'description':'not meat' , 'purchaser':'asma'}
        }) 

        self.assertContains(actual,'chicken burger')   

    def test_update_view(self):
        actual=self.client.post(
            reverse('snack_update',args='1'),
            {'name':'chicken burger' , 'description':'not meat' , 'purchaser':'asma'})
        self.assertRedirects(actual,reverse('snack_list'))    

    def test_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)




        




