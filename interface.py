import flet as ft


def main(page: ft.Page):
    page.controls.clear()

    page.title = 'Churn or not to churn'
    page.bgcolor = ft.colors.WHITE

    # ___Variables___
    width = 400
    reg_01 = r"^[01]$"
    reg_0_or_else = r"^(0|[1-9]\d*)$"

    description = ft.Text(
        value='Welcome!\n'
              'Please enter the data in the appropriate fields and hit execute to find out\n'
              'whether the client will ride off into the sunset or continue consuming the content.',
        size=20,
        color=ft.colors.GREEN
    )

    tv_subscription_status = ft.TextField(
        label="TV Subscription Status",
        input_filter=ft.InputFilter(allow=True, regex_string=reg_01, replacement_string="", ),
        width=width
    )

    movie_package_subscription_status = ft.TextField(
        label="Movie Package Subscription Status",
        input_filter=ft.InputFilter(allow=True, regex_string=reg_01, replacement_string=""),
        width=width
    )

    length_of_subscription = ft.TextField(
        label="Length of Subscription (in months)",
        input_filter=ft.InputFilter(allow=True, regex_string=reg_0_or_else, replacement_string=""),
        width=width
    )

    average_monthly_bill = ft.TextField(
        label="Average Monthly Bill",
        input_filter=ft.InputFilter(allow=True, regex_string=reg_0_or_else, replacement_string=""),
        width=width
    )

    remaining_contract_duration = ft.TextField(
        label="Remaining Contract Duration (in months)",
        input_filter=ft.InputFilter(allow=True, regex_string=reg_0_or_else, replacement_string=""),
        width=width
    )

    number_of_service_failures = ft.TextField(
        label="Number of Service Failures",
        input_filter=ft.InputFilter(allow=True, regex_string=reg_0_or_else, replacement_string=""),
        width=width
    )

    average_download_speed = ft.TextField(
        label="Average Download Speed (Mbps)",
        input_filter=ft.InputFilter(allow=True, regex_string=reg_0_or_else, replacement_string=""),
        width=width
    )

    average_upload_speed = ft.TextField(
        label="Average Upload Speed (Mbps)",
        input_filter=ft.InputFilter(allow=True, regex_string=reg_0_or_else, replacement_string=""),
        width=width
    )

    data_over_limit_usage = ft.TextField(
        label="Data Over Limit Usage",
        input_filter=ft.InputFilter(allow=True, regex_string=reg_0_or_else, replacement_string=""),
        width=width
    )

    fields = [
        tv_subscription_status,
        movie_package_subscription_status,
        length_of_subscription,
        average_monthly_bill,
        remaining_contract_duration,
        number_of_service_failures,
        average_download_speed,
        average_upload_speed,
        data_over_limit_usage,
    ]

    message_container = ft.Container(
        padding=20,
        margin=20,
        bgcolor=ft.colors.BLACK,
        border_radius=10,
        visible=False
    )
    fields_output_container = ft.Container(
        padding=20,
        margin=20,
        bgcolor=ft.colors.BLACK,
        border_radius=10,
        visible=False
    )

    # ___Fields fill check___
    def on_submit(e):
        message_container.content = None
        fields_output_container.content = None
        message_container.visible = False
        fields_output_container.visible = False

        missing_fields = [field.label for field in fields if not field.value.strip()]
        if missing_fields:
            message_container.content = ft.Text(
                f"Please fill in all the required fields: {', '.join(missing_fields)}",
                color=ft.colors.RED
            )
            message_container.visible = True
        else:
            message_container.content = ft.Text("All data entered successfully!", color=ft.colors.GREEN)
            message_container.visible = True

            # nastepny wiersz zakomentuj
            fields_info = "\n".join([f"{field.label}: {field.value.strip()}" for field in fields])
            # w nastepnym wierszu zamiast FIELDS_INFO podstaw zmiena z odpowiedzia modeli
            fields_output_container.content = ft.Text(f"{fields_info}", color=ft.colors.BLUE)
            fields_output_container.visible = True

        page.update()

    # ___Reset Function___
    def on_reset(e):
        for field in fields:
            field.value = ""
        message_container.visible = False
        fields_output_container.visible = False
        page.update()

    # ___Button___
    submit_button = ft.ElevatedButton(text="Submit", on_click=on_submit, width=150, color=ft.colors.BLUE)
    reset_button = ft.ElevatedButton(text="Reset", on_click=on_reset, width=150, color=ft.colors.RED)

    # ___Grid Layout for Fields___
    grid = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    tv_subscription_status,
                    movie_package_subscription_status,
                    length_of_subscription,
                ],
                spacing=20,
            ),
            ft.Row(
                controls=[
                    average_monthly_bill,
                    remaining_contract_duration,
                    number_of_service_failures,
                ],
                spacing=20,
            ),
            ft.Row(
                controls=[
                    average_download_speed,
                    average_upload_speed,
                    data_over_limit_usage,
                ],
                spacing=20,
            ),
        ],
        spacing=20
    )

    # ___Scrollable Content___
    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=description,
                    padding=20,
                    margin=20,
                    bgcolor=ft.colors.BLACK,
                    border_radius=10,
                ),
                grid,
                ft.Row(
                    controls=[submit_button, reset_button],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=20,
                ),
                message_container,
                fields_output_container,
            ]
        )
    )

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)
