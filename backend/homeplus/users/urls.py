
# Explicación de las rutas:
#api/token/: Esta ruta permite obtener un token JWT válido proporcionando las credenciales de usuario (por ejemplo, email y password).
#api/token/refresh/: Esta ruta permite refrescar el token JWT utilizando un token de actualización válido. 

from django.urls import path
from .views import register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import get_user_profile
from .views import crear_proyecto

urlpatterns = [
    path('register/', register, name='register'),  # Esta es tu vista de registro
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Ruta para obtener el token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Ruta para refrescar el token
    path('profile/', get_user_profile, name='user_profile'),
    path('proyectos/', crear_proyecto, name='crear_proyecto'),
]
