window.CI360.init();

function noResultsCheck() {
    var numItems = $grid.isotope('getFilteredItemElements').length;
    console.log(numItems);
    if (numItems == 0) {
        $('.grid-no-elements').show();
    } else {
        $('.grid-no-elements').hide();
    }
}

var $grid = undefined;
var filters = [];

$(document).ready(function () {
    $grid = $('.grid').isotope({
        itemSelector: '.item',
        layoutMode: 'masonry',
        masonry: {
            columnWidth: '.grid-sizer'
        }
    });

    $(".item-filter").click(function (target) {
        var value = "." + target.target.dataset.prop;
        var indexOf = filters.indexOf(value);
        if (indexOf >= 0) {
            filters.pop(indexOf);
            $(target.target).removeClass("active");
        } else {
            filters.push(value);
            $(target.target).addClass("active");
        }
        $grid.isotope({ filter: filters.join("") });
        noResultsCheck();
    })
});


