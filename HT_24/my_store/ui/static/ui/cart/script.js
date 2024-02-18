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
    })
})
