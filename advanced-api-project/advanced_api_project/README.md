Configuration Overview

Views: Uses generics.ListCreateAPIView and generics.RetrieveUpdateDestroyAPIView for efficient, standard CRUD operations.

Serializer: BookSerializer is used, which includes custom validation to prevent setting a publication_year in the future.

Permissions: Permissions are checked per HTTP method using the get_permissions method in each view class.

Endpoints