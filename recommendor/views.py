from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserPreference
from .recommendation import recommend_items

# Create your views here.
@api_view(["GET"])
def get_recommendations(request):
    user_id = request.data.get('user_id')
    user_pref = get_object_or_404(UserPreference, user_id=1)
    print(user_pref)
    recommended_items = recommend_items(user_id, user_pref.preferred_categories)
    print(recommended_items)
    return Response({'user_id': user_id, "recommendations": recommended_items})

@api_view(['POST'])
def save_user_preferences(request):
    user_id = request.data.get('user_id')
    categories = request.data.get('categories',[])
    print(f"{user_id}: {categories}")
    if not categories:
        return Response({'error':'No Categories Provided'}, status=400)
    pref, created = UserPreference.objects.update_or_create(
        user_id=user_id, defaults={'preferred_categories':categories}
    )
    return Response({'message': 'Preference saved successfully'})