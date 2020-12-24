function post_image() {

    var formdata = new FormData()
    var data = $("#send_image").prop("files")[0]
    formdata.append("image", data)


    $.ajax({
        url: "https://ald-api-backend-kxyoqpiojq-nw.a.run.app/predict",
        type: 'POST',
        contentType: false,
        dataType: "json",
        data: formdata,
        processData: false,
        async: true,
        beforeSend: function () {
            document.getElementById("fastapi_status").innerText = "Working";
            document.getElementById("fastapi_status").className = "btn btn-sm btn-warning";
        },
        error: function (xhr, textStatus, error) {
            console.log(xhr.status)
            console.log(error)
            document.getElementById("predicted_class").innerHTML = "--"
            document.getElementById("prediction_likelihood").innerHTML = "--"
            window.alert("The API returned an error!")
            document.getElementById("fastapi_status").innerText = "Error!"
            document.getElementById("fastapi_status").className = "btn btn-sm btn-danger";
        },
        success: function (data, textStatus, xhr) {
            var predicted_class = xhr.responseJSON["predicted_class"]
            var likelihood = xhr.responseJSON["likelihood"]

            document.getElementById("predicted_class").innerHTML = predicted_class
            document.getElementById("prediction_likelihood").innerHTML = (likelihood * 100).toFixed(2) + "%"
            document.getElementById("fastapi_status").innerText = "Complete"
            document.getElementById("fastapi_status").className = "btn btn-sm btn-info";
        },
        complete: function (xhr, textStatus) {
            console.log(xhr.status)
        }
    });
};

function ping_api() {
    document.getElementById("fastapi_status").innerText = "Connecting"
    document.getElementById("fastapi_status").className = "btn btn-sm btn-warn"

    $.ajax({
        url: 'https://ald-api-backend-kxyoqpiojq-nw.a.run.app/',
        success: function (result) {
            document.getElementById("fastapi_status").innerText = "Ready"
            document.getElementById("fastapi_status").className = "btn btn-sm btn-success";
        },
        error: function (result) {
            document.getElementById("fastapi_status").innerText = "Unavailable"
            document.getElementById("fastapi_status").className = "btn btn-sm btn-danger";

        }
    });
};

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#send_image_preview').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]); // convert to base64 string
    }
};

$(function () {
    $(window).ready(ping_api)
    $('#send_image').change(post_image)
    $("#send_image").change(function () {
        readURL(this);
    });
})
