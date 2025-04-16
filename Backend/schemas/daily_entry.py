from extensions  import ma
from models.daily_entry import DailyEntry

class DailyEntrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DailyEntry
        load_instance = True
