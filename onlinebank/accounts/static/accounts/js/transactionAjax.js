
$("#form-button").click(function(e) {
    // serialize form data
    var $serializedFormData = $("#transaction-form").serialize();

    $.post(
        "/accounts/transaction",
        $serializedFormData,
    ).done(
        function (response) {
            $("#transaction-form").trigger("reset")
            $("#transactionModal").modal("hide")
        }
     )    
})

// $("#create-account-form-button").click(function(e) {
//     // serialize form data
//     var $serializedFormData = $("#create-account-form").serialize();

//     $.post(
//         "/accounts/transaction",
//         $serializedFormData,
//     ).done(
//         function (response) {
//             $("#transaction-form").trigger("reset")
//             $("#transactionModal").modal("hide")
//         }
//      )    
// })
