
from models.model import Traline, TralineInfo


class TralineService:

    @staticmethod
    def traline_info_list( traline_id: int):
        return TralineInfo.query.filter_by(traline_id=traline_id).all()

    @staticmethod
    def get_traline(traline_id: int):
        return Traline.query.filter_by(id=traline_id).first()
    @staticmethod
    def get_traline_info(traline_info_id: int):
        return  TralineInfo.query.get(traline_info_id)





