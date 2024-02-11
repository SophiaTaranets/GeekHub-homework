$(document).ready(function () {
    $('.button-delete').on('click', function() {
        let productId = $(this).data('pid');

        $.ajax({
            type: 'DELETE',
            url: '/api/shopping_cart/',
            data: {
                'product_id': productId
            },
            headers: {
                'X-CSRFToken': csrf_token
            },
            success: function(data) {
                console.log(`Product with id - ${productId} was deleted from cart!`)
            },
            error: function(error) {
                console.log(error)
            }
        })
    });

    $('.button-add-to-cart').on('click', function() {
    let productId = $(this).data('pid');

    $.ajax({
        type: 'POST',
        url: '/api/shopping_cart_items/',
        data: {
            'product': productId,
        },
        headers: {
            'X-CSRFToken': csrf_token
        },
        success: function(data) {
            console.log(`Product with id - ${productId} was added to cart!`);
        },
        error: function(error) {
            console.log(error);
        }
    });
    });

    $('.button-update-quantity').on('click', function() {
    let productId = $(this).data('product_id');
    let quantity = $(this).closest('.item').find('.quantity-input').val();
    debugger;
    $.ajax({
        type: 'PATCH',
        url: `/api/shopping_cart_items/${productId}/`,
        data: {
            'amount': quantity,
        },
        headers: {
            'X-CSRFToken': csrf_token
        },
        success: function(data) {
            console.log(`Quantity of product with id - ${productId} was updated to ${quantity}`);
        },
        error: function(error) {
            console.log(error);
        }
    });
    });

    $('#button-clear-cart').on('click', function() {
    $.ajax({
        type: 'DELETE',
        url: '/api/shopping_cart_items/',
        headers: {
            'X-CSRFToken': csrf_token
        },
        success: function(data) {
            console.log('Shopping cart was cleared!');
        },
        error: function(error) {
            console.log(error);
        }
    });
});})

