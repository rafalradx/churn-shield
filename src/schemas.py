from pydantic import BaseModel


class InputData(BaseModel):
    is_tv_subscriber: int
    is_movie_package_subscriber: int
    subscription_age: float
    bill_avg: float
    remaining_contract: float
    service_failure_count: int
    download_avg: float
    upload_avg: float
    download_over_limit: float