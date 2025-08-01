from django.db.models import Sum, F
from django.utils import timezone
from django.utils.formats import number_format
from brands.models import Brand
from categories.models import Category
from products.models import Product
from outflows.models import Outflow


def get_product_metrics():
    # pyrefly: ignore  # missing-attribute
    products = Product.objects.all()
    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_selling_price = sum(product.selling_price * product.quantity for product in products)
    total_quantity = sum(product.quantity for product in products)
    total_profit = sum((product.selling_price - product.cost_price) * product.quantity for product in products)

    return dict(
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        total_selling_price=number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True)
    )


def get_sales_metrics():
    # pyrefly: ignore  # missing-attribute
    outflows = Outflow.objects.all()
    total_products_sold = sum(outflow.quantity for outflow in outflows) or 0
    total_sales_value = sum(outflow.quantity * outflow.product.selling_price for outflow in outflows)
    total_sales_cost = sum(outflow.quantity * outflow.product.cost_price for outflow in outflows)
    total_sales_profit = total_sales_value - total_sales_cost

    # pyrefly: ignore  # no-matching-overload
    return dict(
        total_sales=outflows.count(),
        total_products_sold=total_products_sold,
        total_sales_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    )


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        # pyrefly: ignore  # missing-attribute
        sales_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('product__selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    return dict(
        dates=dates,
        values=values,
    )


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        # pyrefly: ignore  # missing-attribute
        sales_quantity = Outflow.objects.filter(created_at__date=date).count()
        quantities.append(sales_quantity)

    return dict(
        dates=dates,
        values=quantities
    )


def get_product_count_by_category():
    # pyrefly: ignore  # missing-attribute
    categories = Category.objects.all()

    # pyrefly: ignore  # missing-attribute
    return {category.name: Product.objects.filter(category=category).count() for category in categories}


def get_product_count_by_brand():
    # pyrefly: ignore  # missing-attribute
    brands = Brand.objects.all()

    # pyrefly: ignore  # missing-attribute
    return {brand.name: Product.objects.filter(brand=brand).count() for brand in brands}
