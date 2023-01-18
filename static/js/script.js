$(document).ready(function() {
    //SCRIPTS IN HEADER
    $('.burger-btn').click(function(){
        $('.burger-btn').toggleClass('active');
        $('.mobile-menu-container').toggleClass('active');
        $('.mobile-menu').toggleClass('active');
        $('body').toggleClass('scrollable').toggleClass('lock');
    });
    $('.main').click(function(){
        if($('.burger-btn').hasClass('active')){
            $('.burger-btn').removeClass('active');
            $('.mobile-menu-container').removeClass('active');
            $('.mobile-menu').removeClass('active');
            $('body').addClass('scrollable').removeClass('lock');
        }
    });

    $(window).scroll(function(){
        if($(document).scrollTop()>50){
            $('header').addClass('scrolled');
        }
        else if($(document).scrollTop()<=50){
            $('header').removeClass('scrolled');
        }
    });

    $('.search-btn').click(function () {
        $('.search').toggleClass('visible');
        $('.login-btn').toggleClass('hidden');
    });
    $('.info-item').click(function () {
        $(this).find('.dropdown').toggleClass('visible');
        $(this).toggleClass('active');
    });
    $('.info-btn').click(function () {
        $(this).siblings('.dropdown').toggleClass('open');
        $(this).find('.item-arrow').toggleClass('open');
    });

    //END OF SCRIPTS IN HEADER


    //SCRIPTS IN FORMS
    $('.placeholder').click(function() {
        $(this).siblings('input').focus();
    });
    $('.input').blur(function() {
        var input = $(this);
        if (input.val().length == 0) {
            input.siblings('.placeholder').show();
        }
    });
    $('.input').on('input', function() {
        var input = $(this);
        if (input.val().length == 0){
            input.siblings('.placeholder').show();
        }
        else{
            input.siblings('.placeholder').hide();
        }
    });
    $('.input').blur();
    //END OF SCRIPTS IN FORMS



    //SCRIPTS IN MODALS
    $('.error .close').click(function () {
        var parent = $(this).parent();
        parent.addClass('hidden');
        setTimeout(function () {
            parent.addClass('none');
        }, 350);
    });
    //END OF SCRIPTS IN MODALS



    // SPOILER SCRIPTS

    $('.spoiler-heading').click(function () {
        if($(window).width()<=1200){
            $(this).toggleClass('active').next().slideToggle(300,"linear");
        }
    });

    // END OF SPOILER SCRIPTS


    //CUSTOM SELECT SCRIPTS

    var x, i, j, l, ll, selElmnt, a, b, c;
    /* Look for any elements with the class "custom-select": */
    x = document.getElementsByClassName("custom-select");
    l = x.length;
    for (i = 0; i < l; i++) {
        selElmnt = x[i].getElementsByTagName("select")[0];
        ll = selElmnt.length;
        /* For each element, create a new DIV that will act as the selected item: */
        a = document.createElement("DIV");
        a.setAttribute("class", "select-selected");
        a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
        x[i].appendChild(a);
        /* For each element, create a new DIV that will contain the option list: */
        b = document.createElement("DIV");
        b.setAttribute("class", "select-items select-hide");
        for (j = 1; j < ll; j++) {
            /* For each option in the original select element,
            create a new DIV that will act as an option item: */
            c = document.createElement("DIV");
            c.innerHTML = selElmnt.options[j].innerHTML;
            c.addEventListener("click", function(e) {
                /* When an item is clicked, update the original select box,
                and the selected item: */
                var y, i, k, s, h, sl, yl;
                s = this.parentNode.parentNode.getElementsByTagName("select")[0];
                sl = s.length;
                h = this.parentNode.previousSibling;
                for (i = 0; i < sl; i++) {
                    if (s.options[i].innerHTML == this.innerHTML) {
                        s.selectedIndex = i;
                        h.innerHTML = this.innerHTML;
                        y = this.parentNode.getElementsByClassName("same-as-selected");
                        yl = y.length;
                        for (k = 0; k < yl; k++) {
                            y[k].removeAttribute("class");
                        }
                        this.setAttribute("class", "same-as-selected");
                        break;
                    }
                }
                h.click();
            });
            b.appendChild(c);
        }
        x[i].appendChild(b);
        a.addEventListener("click", function(e) {
            /* When the select box is clicked, close any other select boxes,
            and open/close the current select box: */
            e.stopPropagation();
            closeAllSelect(this);
            this.nextSibling.classList.toggle("select-hide");
            this.classList.toggle("select-arrow-active");
        });
    }

    function closeAllSelect(elmnt) {
        /* A function that will close all select boxes in the document,
        except the current select box: */
        var x, y, i, xl, yl, arrNo = [];
        x = document.getElementsByClassName("select-items");
        y = document.getElementsByClassName("select-selected");
        xl = x.length;
        yl = y.length;
        for (i = 0; i < yl; i++) {
            if (elmnt == y[i]) {
                arrNo.push(i)
            } else {
                y[i].classList.remove("select-arrow-active");
            }
        }
        for (i = 0; i < xl; i++) {
            if (arrNo.indexOf(i)) {
                x[i].classList.add("select-hide");
            }
        }
    }

    /* If the user clicks anywhere outside the select box,
    then close all select boxes: */
    document.addEventListener("click", closeAllSelect);
    //END OF CUSTOM SELECT SCRIPTS

    // MODAL SCRIPTS
    $('.message').on('shown.bs.modal', function (event) {
        setTimeout(function () {
            $('.message').modal('hide');
        }, 5000);
    });
    // END OF MODAL SCRIPTS

    // QUANTITY INPUTS SCRIPTS
    $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });
    $('[name="quantity"]').change(function () {
        var price_new;
        var quantity = $(this).val();
            var price = $(this).parents('.product-row').find('.price .value').text();
            price_new = toNumberWithoutDelimiters(price)*quantity;
            $(this).parents('.product-row').find('.overall-price .value').html(toNumberWithDelimiters(price_new));

    });
    function toNumberWithoutDelimiters(x) {
        return parseInt(x.toString().replace(/\s/g, ""));
    }
    function toNumberWithDelimiters(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    }
    //END OF QUANTITY INPUTS SCRIPTS

});
//FILTER RANGE SCRIPTS
function initializeRangeSlider(minimum, maximum){
    var pricesSlider = document.getElementById('range-slider');

    noUiSlider.create(pricesSlider, {
        start: [0, 10000],
        range: {
            'min': [minimum],
            'max': [maximum]
        },
        step: 100,
    });
    pricesSlider.noUiSlider.on('update', function () {
        $('#min').val(Math.round(pricesSlider.noUiSlider.get()[0]));
        $('#max').val(Math.round(pricesSlider.noUiSlider.get()[1]));
    });
    $('#min').on('input', function() {
        pricesSlider.noUiSlider.set([$('#min').val(), null], true, true);
    });
    $('#max').on('input', function() {
        pricesSlider.noUiSlider.set([null, $('#max').val()]);
    });
}
//END OF FILTER RANGE SCRIPTS
