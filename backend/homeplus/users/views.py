from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Proyecto  # Import your custom User and Proyecto models
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse JSON data
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Validate required fields
        if not name or not email or not password:
            return JsonResponse({'error': 'Faltan campos obligatorios'}, status=400)

        # Check if a user with the same email already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'El correo ya está registrado'}, status=400)

        # Create the user using the CustomUserManager
        user = User.objects.create_user(email=email, name=name, password=password)

        # Return success response
        return JsonResponse({'message': 'Usuario registrado con éxito'}, status=201)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    return Response({
        'name': user.name,
        'email': user.email,
        'is_worker': user.is_worker,
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_proyecto(request):
    if request.user.is_worker:
        return Response({'error': 'Los trabajadores no pueden crear proyectos'}, status=400)

    data = request.data
    titulo = data.get('titulo')
    descripcion = data.get('descripcion')

    if not titulo or not descripcion:
        return Response({'error': 'Faltan campos obligatorios'}, status=400)

    # Create the project
    proyecto = Proyecto.objects.create(titulo=titulo, descripcion=descripcion, cliente=request.user)
    return Response({'message': 'Proyecto creado con éxito'}, status=201)