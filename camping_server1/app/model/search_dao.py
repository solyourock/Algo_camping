from dataclasses import dataclass
from sqlalchemy import Column
from ..model import db


@dataclass
class SearchDAO(db.Model):

    __tablename__ = 'search'
    __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'}

    id = Column(db.Integer, primary_key=True)
    place_name = Column(db.String(255), primary_key=False)
    content_id = Column(db.Integer, primary_key=False)
    addr = Column(db.String(255), primary_key=False)
    tag = Column(db.String(255), primary_key=False)

    fun_m = Column(db.Integer, primary_key=False)
    comfort_m = Column(db.Integer, primary_key=False)
    together_m = Column(db.Integer, primary_key=False)
    natural_m = Column(db.Integer, primary_key=False)
    activity_m = Column(db.Integer, primary_key=False)

    ecological_s = Column(db.Integer, primary_key=False)
    walkway_s = Column(db.Integer, primary_key=False)
    festival_s = Column(db.Integer, primary_key=False)
    cultural_s = Column(db.Integer, primary_key=False)
    hot_water_s = Column(db.Integer, primary_key=False)
    clean_s = Column(db.Integer, primary_key=False)
    parking_car_s = Column(db.Integer, primary_key=False)
    spacious_s = Column(db.Integer, primary_key=False)
    with_child_s = Column(db.Integer, primary_key=False)
    with_family_s = Column(db.Integer, primary_key=False)
    with_couple_s = Column(db.Integer, primary_key=False)
    with_dog_s = Column(db.Integer, primary_key=False)
    valley_s = Column(db.Integer, primary_key=False)
    pure_water_s = Column(db.Integer, primary_key=False)
    starry_s = Column(db.Integer, primary_key=False)
    healing_s = Column(db.Integer, primary_key=False)
    play_water_s = Column(db.Integer, primary_key=False)
    bicycle_s = Column(db.Integer, primary_key=False)
    pool_s = Column(db.Integer, primary_key=False)
    extreme_s = Column(db.Integer, primary_key=False)

    def __init__(self, place_name, content_id, addr, tag, fun_m, comfort_m, together_m, natural_m, activity_m, ecological_s,
                 walkway_s, festival_s, cultural_s, hot_water_s, clean_s, parking_car_s, spacious_s,
                 with_child_s, with_family_s, with_couple_s, with_dog_s, valley_s, pure_water_s, starry_s, healing_s,
                 play_water_s, bicycle_s, pool_s, extreme_s):
        self.place_name = place_name
        self.content_id = content_id
        self.addr = addr
        self.tag = tag

        self.fun_m = fun_m
        self.comfort_m = comfort_m
        self.together_m = together_m
        self.natural_m = natural_m
        self.activity_m = activity_m
        self.ecological_s = ecological_s

        self.walkway_s = walkway_s,
        self.festival_s = festival_s
        self.cultural_s = cultural_s
        self.hot_water_s = hot_water_s
        self.clean_s = clean_s
        self.parking_car_s = parking_car_s
        self.spacious_s = spacious_s
        self.with_child_s = with_child_s
        self.with_family_s = with_family_s
        self.with_couple_s = with_couple_s
        self.with_dog_s = with_dog_s
        self.valley_s = valley_s
        self.pure_water_s = pure_water_s
        self.starry_s = starry_s
        self.healing_s = healing_s
        self.play_water_s = play_water_s
        self.bicycle_s = bicycle_s
        self.pool_s = pool_s
        self.extreme_s = extreme_s

db.create_all()