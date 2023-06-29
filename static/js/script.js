$(document).ready(function () {
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav',
        adaptiveHeight: true,
        initialSlide: 2,
    });
    $('.slider-nav').slick({
        arrows: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: false,
        centerMode: true,
        focusOnSelect: true,
        adaptiveHeight: true,
        speed: 1000,
        initialSlide: 2,
        autoplay: true,
        autoplaySpeed: 1500,
        variableWidth: true,
        responsive:[
            {
                breakpoint: 576,
                settings: {
                    slidesToShow:3,
                    arrows: false
                }
            },
            {
                breakpoint: 1140,
                settings: {
                    slidesToShow:4
                }
            }
        ]
    });
});

Fancybox.bind("[data-fancybox]", {
    // Your custom options
});
