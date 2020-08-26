from django.db import models

# Create your models here.
class Course(models.Model):
    """Model definition for Course."""

    # TODO: Define fields here
    title = models.CharField(null=False, max_length=50, verbose_name="Título")
    description = models.CharField(null=False, max_length=500, verbose_name="Descripción")
    uploaded = models.DateField(null=False, auto_now=True, verbose_name='Fecha de publicación')
    facephoto = models.ImageField(null=True, blank=True, upload_to='profilephoto', verbose_name="Foto de perfil")


    class Meta:
        """Meta definition for Course."""

        ordering = ['title', 'uploaded']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        """Unicode representation of Course."""
        return self.title


class Instructor(models.Model):
    """Model definition for Instructors."""

    # TODO: Define fields here
    fullname = models.CharField(null=False, max_length=50, verbose_name='Nombre completo')
    grade = models.CharField(null=False, max_length=20, verbose_name='Grado')
    uploaded = models.DateField(null=False, auto_now=True, verbose_name='Fecha de publicación')
    facephoto = models.ImageField(null=True, blank=True, upload_to='profilephoto', verbose_name="Foto de perfil")
    courses = models.ManyToManyField(Course, blank=True, related_name='instructors', related_query_name='instructor')

    class Meta:
        """Meta definition for Instructors."""

        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'

    def __str__(self):
        """Unicode representation of Instructors."""
        return f"{self.grade} {self.fullname}"

class Comment(models.Model):
    """Model definition for Comment."""

    # TODO: Define fields here
    student = models.CharField(null=False, max_length=50, verbose_name='Estudiante')
    score = models.IntegerField(null=False, verbose_name='Puntuación')
    comment = models.CharField(null=True, blank=True, max_length=500, verbose_name='Comentario')
    uploaded = models.DateField(null=False, auto_now=True, verbose_name='Fecha de publicación')
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        """Unicode representation of Comment."""
        return f"{self.student}: {self.comment}"

class Price(models.Model):
    """Model definition for Price."""

    # TODO: Define fields here
    actual_price = models.DecimalField(null=False, max_digits=15, decimal_places=2)
    promo = models.DecimalField(null=False, default=0, max_digits=3, decimal_places=2)
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='price', related_query_name='price')

    class Meta:
        """Meta definition for Price."""

        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'

    def __str__(self):
        """Unicode representation of Price."""
        return f"{self.actual_price}$"
