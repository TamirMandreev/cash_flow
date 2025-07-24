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


def prepare_transaction_form_fields(form):
    '''
    Настраивает поля формы для транзакций, ограничивая доступные варианты
    :param form:
    :return:
    '''
    form.fields['category'].queryset = Category.objects.none()
    form.fields['subcategory'].queryset = SubCategory.objects.none()

    if 'operation_type' in form.data:
        operation_type_id = int(form.data.get('operation_type'))
        form.fields['category'].queryset = Category.objects.filter(operation_type_id=operation_type_id).order_by('name')

    if 'category' in form.data:
        category_id = int(form.data.get('category'))
        form.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('name')

    return form