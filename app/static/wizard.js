var customARGB = $("#customARGB");

// Simple example, see optional options for more configuration.
const pickr = Pickr.create({
    el: '.pickr-container',
    theme: 'classic', // or 'monolith', or 'nano'
    inline: true,
    comparison: true,
    showAlways: true,
    swatches: [
        'rgba(244, 67, 54, 1)',
        'rgba(233, 30, 99, 0.95)',
        'rgba(156, 39, 176, 0.9)',
        'rgba(103, 58, 183, 0.85)',
        'rgba(63, 81, 181, 0.8)',
        'rgba(33, 150, 243, 0.75)',
        'rgba(3, 169, 244, 0.7)',
        'rgba(0, 188, 212, 0.7)',
        'rgba(0, 150, 136, 0.75)',
        'rgba(76, 175, 80, 0.8)',
        'rgba(139, 195, 74, 0.85)',
        'rgba(205, 220, 57, 0.9)',
        'rgba(255, 235, 59, 0.95)',
        'rgba(255, 193, 7, 1)'
    ],

    components: {

        // Main components
        preview: true,
        opacity: true,
        hue: true,

        // Input / output Options
        interaction: {
            hex: true,
            rgba: true,
            // hsla: true,
            // hsva: true,
            // cmyk: true,
            input: true,
            clear: true,
            save: true
        }
    }
});

pickr.on('change', instance => {
    $("#argbMode11").attr("checked", true);
    var rgba = instance.toRGBA();
    var r = parseInt(rgba[0]);
    var g = parseInt(rgba[1]);
    var b = parseInt(rgba[2]);
    var a = parseInt(rgba[3]);
    var f = r + "#" + g +  "#" + b;
    customARGB.val(f);
});

function changeWT() {
    var wt = prompt("Please Enter WAIT_TIME (10 is default): ")
    if(wt != '' || wt != null)
    {
        $.ajax(
           {
            url: "/changeWT",
            type: "POST",
            async: false,
            data: {
                "WT": wt
            },
            success: function(d)
            {
                alert("Signal Sent")
            }
           }
        );
    }
}