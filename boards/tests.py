# from django.test import TestCase
from test_plus.test import TestCase
from django.conf import settings
from .models import Board
from .forms import BoardForm


class SettingsTest(TestCase):
    def test_01_settings(self):
        self.assertEqual(settings.USE_I18N, True)
        self.assertEqual(settings.USE_TZ, False)
        self.assertEqual(settings.LANGUAGE_CODE, 'ko-kr')
        self.assertEqual(settings.TIME_ZONE, 'Asia/Seoul')
        
# 2. Model test
class BoardModelTest(TestCase):
    def test_01_model(self):
        board = Board.objects.create(title='test title', content='test content', user_id=1)
        self.assertEqual(str(board), f'Board{board.pk}', msg='출력 값이 일치하지 않음')
        
# 3. View test
class BoardViewTest(TestCase):
    # 공통적인 given 상황을 구성하기에 setUP이 있어 유용함..
    def setUp(self):
        user = self.make_user(username='test', password='qawsedrf!')
    
    
    # create test에서의 포인트는 form을 제대로 주느냐이다. 가장 기본은 get_check_200(성공했는지 보는거)
    def test_01_get_create(self):
        # given
        # user = self.make_user(username='test', password='qawsedrf!')
        # when
        with self.login(username='test', password='qawsedrf!'):
            response = self.get_check_200('boards:create')
            # then
            self.assertIsInstance(response.context['form'], BoardForm)
        
    def test_02_get_create_login_required(self):
        self.assertLoginRequired('boards:create')
        
    def test_03_post_create(self):
        # given 사용자와 작성한 글 데이터
        # user = self.make_user(username='test', password='qawsedrf!')
        data = {'title': 'test title', 'content' : 'test content'}
        # when 로그인을 해서 post요청으로 해당 url로 요청 보낸 경우
        with self.login(username='test', password='qawsedrf!'):
            # then 글이 작성되고 디테일 페이지로 가는지.
            self.post('boards:create', data=data)
    
    def test_04_board_create_without_content(self):
        # given 
        data = {'title' : 'test title'}
        # when
        with self.login(username='test', password='qawsedrf!'):
            response = self.post('boards:create', data=data)
            self.assertContains(response, '필수 항목입니다.!')
            # form.is_valid() 를 통과하지 못해서 튕겨저 나옴.
            # assertContains response 해당하는 글자가 있는 확인하는 메소드
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        