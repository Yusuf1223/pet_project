$(window).resize(function() {

    // $('.owl-dot').each(function(){
    //     $(this).text($(this).index()+1);
    // });
});
$(document).ready(function(){
    var main_slider = $('.owl-carousel#main-slider');
    main_slider.owlCarousel({
        // nav:true,
        // navContainer: '.tabs-navigation',
        items: 1,
        margin:0,
        loop: true,
        autoplay:true,
        autoplayTimeout:3000,
        autoplayHoverPause:true,
        lazyLoad: true,
        onInitialized: counter,
        onChanged: counter,
        responsive: {
            // 0:{
            //     items: 3,
            // },
            // 1251:{
            //     items: 4,
            // },
        }
    });
    $('.slider-forward').click(function() {
        main_slider.trigger('next.owl.carousel');
    });
    $('.slider-back').click(function() {
        main_slider.trigger('prev.owl.carousel', [300]);
    });

    function counter(event) {
        if (!event.namespace) {
            return;
        }
        var slides = event.relatedTarget;
        $('.slider-counter .current').text(slides.relative(slides.current()) + 1);
        $('.slider-counter .overall').text(slides.items().length);
    }


    var product_slider = $('.owl-carousel#product-slider');
    product_slider.owlCarousel({
        items: 1,
        margin:0,
        dots: true,
        onTranslated: dots_scroll,
    });
    $('.product-slider-forward').click(function() {
        product_slider.trigger('next.owl.carousel');
    });
    $('.product-slider-back').click(function() {
        product_slider.trigger('prev.owl.carousel', [300]);
    });


    dotcount = 1;

    $('.owl-dot').each(function() {
        $( this ).addClass( 'dotnumber' + dotcount);
        $( this ).attr('data-info', dotcount);
        dotcount=dotcount+1;
    });

    slidecount = 1;

    $('.owl-item').not('.cloned').each(function() {
        $( this ).addClass( 'slidenumber' + slidecount);
        // $(this).attr('id', slidecount);
        slidecount=slidecount+1;
    });
    $('.owl-dot').each(function() {
        grab = jQuery(this).data('info');
        slidegrab = jQuery('.slidenumber'+ grab +' img').attr('src');
        $(this).css("background-image", "url("+slidegrab+")");
    });

});
function dots_scroll() {
    var activeDot = document.querySelectorAll('.owl-dot.active')[0];
    var dotsContainer = document.querySelectorAll('.owl-dots')[0];
    var activeDotOffset = activeDot.offsetTop;
    var activeDotOffsetLeft = activeDot.offsetLeft;
    var windowWidth = window.innerWidth;
    if(windowWidth > 768){
        if(activeDotOffset>775){
            dotsContainer.scrollBy({
                left: 0,
                top: 194,
                behavior: 'smooth',
            });
        }
        if(activeDotOffset<775 && dotsContainer.scrollTop > 20){
            dotsContainer.scrollTo({
                left: 0,
                top: activeDotOffset,
                behavior: 'smooth',
            });
        }
    }
    else if(windowWidth <= 768 && windowWidth > 576){
        if(activeDotOffsetLeft>(windowWidth - 70)){
            dotsContainer.scrollBy({
                left: 85,
                top: 0,
                behavior: 'smooth',
            });
        }
        if(activeDotOffset<(windowWidth - 70) && dotsContainer.scrollLeft > 20){
            dotsContainer.scrollTo({
                left: activeDotOffsetLeft,
                top: 0,
                behavior: 'smooth',
            });
        }
    }
    else if(windowWidth <= 576){
        if(activeDotOffsetLeft>(windowWidth - 60)){
            dotsContainer.scrollBy({
                left: 85,
                top: 0,
                behavior: 'smooth',
            });
        }
        if(activeDotOffset<(windowWidth - 60) && dotsContainer.scrollLeft > 20){
            dotsContainer.scrollTo({
                left: activeDotOffsetLeft,
                top: 0,
                behavior: 'smooth',
            });
        }
    }
}
