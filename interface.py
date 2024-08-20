import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import flet as ft
import joblib
import pandas as pd
from tensorflow.keras.models import load_model

# ___Loading Models & Scaler___
scaler = joblib.load("models/scaler.pkl")
model_rf = joblib.load("models/random_forest_classifier.pkl")
model_dnn = load_model("models/dense_neural_net_classifier.keras")

# Scaler features
features_to_scale = [
    "subscription_age",
    "bill_avg",
    "reamining_contract",
    "service_failure_count",
    "download_avg",
    "upload_avg",
]

correct_feature_order = [
    "is_tv_subscriber",
    "is_movie_package_subscriber",
    "subscription_age",
    "bill_avg",
    "reamining_contract",
    "service_failure_count",
    "download_avg",
    "upload_avg",
    "download_over_limit",
]


def main(page: ft.Page):
    page.controls.clear()

    page.title = "Churn or not to churn"
    page.bgcolor = "#fcde67"

    # ___Variables___
    width = 500
    reg_float_or_int = r"^(0|[1-9]\d*|0\.\d*|[1-9]\d*\.\d*)$"

    text_style = ft.TextStyle(
        color="#030e12",
    )

    text_field_label_style = ft.TextStyle(
        color="#030e12",
    )

    description = ft.Text(
        value="Welcome!\n"
        "Please enter the data in the appropriate fields and hit execute to find out\n"
        "whether the client will ride off into the sunset or continue consuming the content.",
        size=17,
        color=ft.colors.BLACK,
    )

    # ___Checkboxes___
    tv_subscription_status = ft.Checkbox(
        label="TV Subscription Status",
        label_style=ft.TextStyle(color="#030e12"),
        value=False,
        fill_color="#030e12",
        check_color="#fcde67",
    )

    movie_package_subscription_status = ft.Checkbox(
        label="Movie Package Subscription Status",
        label_style=ft.TextStyle(color="#030e12"),
        value=False,
        fill_color="#030e12",
        check_color="#fcde67",
    )

    # ___TextFields___
    length_of_subscription = ft.TextField(
        label="Length of Subscription (in months)",
        label_style=ft.TextStyle(color="#030e12"),
        input_filter=ft.InputFilter(
            allow=True, regex_string=reg_float_or_int, replacement_string=""
        ),
        width=width,
        bgcolor=ft.colors.WHITE,
        border_color="#5bccf6",
        border_radius=10,
        text_style=text_style,
    )

    average_monthly_bill = ft.TextField(
        label="Average Monthly Bill ($$$)",
        label_style=ft.TextStyle(color="#030e12"),
        input_filter=ft.InputFilter(
            allow=True, regex_string=reg_float_or_int, replacement_string=""
        ),
        width=width,
        bgcolor=ft.colors.WHITE,
        border_color="#5bccf6",
        border_radius=10,
        text_style=text_style,
    )

    remaining_contract_duration = ft.TextField(
        label="Remaining Contract Duration (in months)",
        label_style=ft.TextStyle(color="#030e12"),
        input_filter=ft.InputFilter(
            allow=True, regex_string=reg_float_or_int, replacement_string=""
        ),
        width=width,
        bgcolor=ft.colors.WHITE,
        border_color="#5bccf6",
        border_radius=10,
        text_style=text_style,
    )

    number_of_service_failures = ft.TextField(
        label="Number of Service Failures (times)",
        label_style=ft.TextStyle(color="#030e12"),
        input_filter=ft.InputFilter(
            allow=True, regex_string=reg_float_or_int, replacement_string=""
        ),
        width=width,
        bgcolor=ft.colors.WHITE,
        border_color="#5bccf6",
        border_radius=10,
        text_style=text_style,
    )

    average_download_speed = ft.TextField(
        label="Average Download Speed (Mbps)",
        label_style=ft.TextStyle(color="#030e12"),
        input_filter=ft.InputFilter(
            allow=True, regex_string=reg_float_or_int, replacement_string=""
        ),
        width=width,
        bgcolor=ft.colors.WHITE,
        border_color="#5bccf6",
        border_radius=10,
        text_style=text_style,
    )

    average_upload_speed = ft.TextField(
        label="Average Upload Speed (Mbps)",
        label_style=ft.TextStyle(color="#030e12"),
        input_filter=ft.InputFilter(
            allow=True, regex_string=reg_float_or_int, replacement_string=""
        ),
        width=width,
        bgcolor=ft.colors.WHITE,
        border_color="#5bccf6",
        border_radius=10,
        text_style=text_style,
    )

    data_over_limit_usage = ft.TextField(
        label="Data Over Limit Usage (times)",
        label_style=ft.TextStyle(color="#030e12"),
        input_filter=ft.InputFilter(
            allow=True, regex_string=reg_float_or_int, replacement_string=""
        ),
        width=width,
        bgcolor=ft.colors.WHITE,
        border_color="#5bccf6",
        border_radius=10,
        text_style=text_style,
    )

    fields = [
        length_of_subscription,
        average_monthly_bill,
        remaining_contract_duration,
        number_of_service_failures,
        average_download_speed,
        average_upload_speed,
        data_over_limit_usage,
    ]

    # ___Containers___
    welcome_message_conteiner = ft.Container(
        content=description,
        padding=20,
        margin=5,
        bgcolor="#5bccf6",
        border_radius=15,
    )

    message_container = ft.Container(
        padding=20,
        margin=5,
        bgcolor="#030e12",
        border_radius=15,
        visible=False,
    )

    display_data_conteiner = ft.Container(
        padding=20,
        margin=5,
        bgcolor="#030e12",
        border_radius=15,
        visible=False,
    )

    results_container = ft.Container(
        padding=20,
        margin=5,
        bgcolor="#030e12",
        border_radius=15,
        visible=False,
    )

    # ___Fields fill check___
    def on_submit(e):
        message_container.content = None
        display_data_conteiner.content = None
        results_container.content = None
        message_container.visible = False
        display_data_conteiner.visible = False
        results_container.visible = False

        missing_fields = [
            field.label
            for field in fields
            if isinstance(field.value, str) and not field.value.strip()
        ]
        if missing_fields:
            message_container.content = ft.Text(
                f"Please fill in all the required fields:\n"
                + ",\n".join(missing_fields),
                color=ft.colors.RED,
            )
            message_container.visible = True
        else:
            tv_status_display = (
                "Subscription" if tv_subscription_status.value else "NO Subscription"
            )
            movie_status_display = (
                "Subscription"
                if movie_package_subscription_status.value
                else "NO Subscription"
            )

            fields_info = (
                f"All data entered successfully!\n"
                f"TV Subscription Status: {tv_status_display}\n"
                f"Movie Package Subscription Status: {movie_status_display}\n"
                + "\n".join(
                    [f"{field.label}: {field.value.strip()}" for field in fields]
                )
            )

            display_data_conteiner.content = ft.Text(
                f"{fields_info}", color=ft.colors.WHITE
            )
            display_data_conteiner.visible = True

            # Prepare the data for the model
            new_data = {
                "is_tv_subscriber": float(tv_subscription_status.value),
                "is_movie_package_subscriber": float(
                    movie_package_subscription_status.value
                ),
                "subscription_age": float(length_of_subscription.value.strip()),
                "bill_avg": float(average_monthly_bill.value.strip()),
                "reamining_contract": float(remaining_contract_duration.value.strip()),
                "service_failure_count": float(
                    number_of_service_failures.value.strip()
                ),
                "download_avg": float(average_download_speed.value.strip()),
                "upload_avg": float(average_upload_speed.value.strip()),
                "download_over_limit": float(data_over_limit_usage.value.strip()),
            }

            df = pd.DataFrame(
                [[new_data[feature] for feature in correct_feature_order]],
                columns=correct_feature_order,
            )
            df[features_to_scale] = scaler.transform(df[features_to_scale])

            random_forest_probability = model_rf.predict_proba(df)[:, 1][0]
            dense_neural_net_probability = model_dnn.predict(df.values)[0][0]

            random_forest_results = round(random_forest_probability * 100, 2)
            dense_neural_net_results = round(dense_neural_net_probability * 100, 2)

            results_container.content = ft.Text(
                f"Quiting probability for\n"
                f"Random Forest is {random_forest_results}%\n"
                f"Dense Nural Net is {dense_neural_net_results}%",
                size=20,
                color=ft.colors.WHITE,
            )
            results_container.visible = True

        page.update()

    # ___Reset Function___
    def on_reset(e):
        for field in fields:
            field.value = ""
        tv_subscription_status.value = False
        movie_package_subscription_status.value = False
        message_container.visible = False
        display_data_conteiner.visible = False
        page.update()

    # ___Button___
    submit_button = ft.ElevatedButton(
        text="Submit", on_click=on_submit, width=150, color="#030e12", bgcolor="#5bccf6"
    )
    reset_button = ft.ElevatedButton(
        text="Reset", on_click=on_reset, width=150, color="#030e12", bgcolor="#5bccf6"
    )

    # ___Controls Column___
    controls_column = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    tv_subscription_status,
                    movie_package_subscription_status,
                ],
                spacing=25,
            ),
            *fields,
            ft.Row(
                controls=[submit_button, reset_button],
                spacing=50,
            ),
            display_data_conteiner,
            message_container,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # ___Content Column___
    content_column = ft.Column(
        controls=[
            welcome_message_conteiner,
            results_container,
            # Tu lozyc kontener z odpowiedziami ML
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30,
    )

    # ___Scrollable Content___
    page.add(
        ft.Row(
            controls=[
                controls_column,
                content_column,
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=30,
        )
    )

    page.update()


ft.app(target=main)
