from cash_flow.models import Category, SubCategory


def load_categories(operation_type_id):
    '''
    Получает список категорий по заданному типу операции
    :param operation_type_id: id типа операции. Модель OperationType
    :return: queryset
    '''
    return Category.objects.filter(operation_type_id=operation_type_id).order_by('name')


def load_subcategories(category_id):
    '''
    Получает список подкатегорий по заданной категории
    :param category_id: id категории. Модель Category
    :return: queryset
    '''
    return SubCategory.objects.filter(category_id=category_id).order_by('name')
