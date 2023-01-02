import graphene

from graphene_django import DjangoObjectType
from BrutalBlogAdmin import models


class PostType(DjangoObjectType):
    class Meta:
        model = models.Blogpost


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.Blogpost.objects.all()
        )

    def resolve_post_by_id(root, info, id):
        return (
            models.Blogpost.objects.get(id=id)
        )


schema = graphene.Schema(query=Query)
