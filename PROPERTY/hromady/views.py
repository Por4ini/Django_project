from django.shortcuts import render
from .models import CommunityHromady


def community(requrst):
    community = CommunityHromady.objects.all()
    title = 'Громади'
    return render(requrst, 'hromady/hromady.html', {'community': community, 'title': title})