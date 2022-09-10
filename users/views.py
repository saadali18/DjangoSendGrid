from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer
from .utils import send_email


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        send_email(
            to=[data["email"]],
            reply_to=[],
            template_id="Your Template ID",
            data={
                "first_name": data["first_name"],
                "last_name": data["last_name"],
            },
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)