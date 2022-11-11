from django.db import models


def test():
    print("test")


class InterceptorQuerySet(models.QuerySet):
    def group_by(self, **kwargs):
        kwargs
        # user_id = kwargs.pop("user_id")

        super(InterceptorQuerySet, self).__init__()


class InterceptorManager(models.Manager):

    def group_by(self, **kwargs):
        return "hola"
        return self.get_queryset(**kwargs)

    def get_queryset(self, **kwargs):
        return InterceptorQuerySet(model=self.model, using=self._db, hints=self._hints, **kwargs)


class PruebaMysql(models.Model):
    created_at = models.DateField(auto_now=True)
    objects = InterceptorManager()

    class Meta:
        abstract = True

    @classmethod
    def group_by(cls):
        return "Hola"