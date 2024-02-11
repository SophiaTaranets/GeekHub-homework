$(document).ready(function () {
    $('#add-to-cart-btn').on('click', function() {
        let productId = $(this).data('pid');

        $.ajax({
            type: 'POST',
            url: '/api/products/',
            data: {
                'product_id': productId
            },
            headers: {
                'X-CSRFToken': csrf_token
            },
            success: function(data) {
                console.log(`Product with id - ${productId} was added to cart!`)
            },
            error: function(error) {
                console.log(error)
            }
        })
    })
})