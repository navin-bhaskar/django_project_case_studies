from rest_framework import routers
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Book
from api.serializer import BookItemSerializer


# class BookListView(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookItemSerializer


class ListCreateBookApiView(APIView):
    serializer_class = BookItemSerializer

    http_method_names = [
        "post",
        "get",
        "delete",
        "patch",
        "head",
        "options",
    ]

    def get(self, request):
        books = Book.objects.all()
        serialized = BookItemSerializer(books, many=True)
        return Response({"response": serialized.data})

    def post(self, request):
        # print(request.data)
        book = BookItemSerializer(data=request.data)
        if not book.is_valid():
            return Response(book.errors, status=400)
        book.save()
        return Response(book.data, status=200)

    def delete(self, request):
        ids = request.query_params.get("ids").split(",")
        print(request.data)
        if ids:
            queryset = Book.objects.filter(id__in=ids)
            queryset.delete()
        return Response("Book deleted")

    def patch(self, request):
        book_item = BookItemSerializer(request.data)
        # print(book_item.data["id"])
        # return Response("Done")
        book_id = book_item.data["id"]
        book = Book.objects.filter(id=book_id).first()
        print(book)

        ser = BookItemSerializer(instance=book, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response("Done")
        else:
            return Response("Invaiid option passed", status=400)
