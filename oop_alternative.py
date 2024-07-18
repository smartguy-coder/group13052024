from dataclasses import dataclass, field
import uuid


# class Parcel:
#     parcel_id: str
#     recipient_name: str
#
#
# p = Parcel()
# p.parcel_id = 'ldhgkjhdf'
# p.recipient_name = 'ejhguergherugh'
# p.gggg = 'kjkjjkj'
#
# print(p.__dict__)


def get_parcel_id():
    return str(uuid.uuid4())


@dataclass(frozen=True)
class Parcel:
    recipient_name: str
    # parcel_id: str = field(default='6745674586745896745968495679')
    parcel_id: uuid.UUID = field(default_factory=get_parcel_id)

    def validate(self):
        if self.recipient_name == 'Ben Laden':
            print('Call CIA')

    def __post_init__(self):
        self.validate()


p = Parcel( recipient_name='Ben Laden')
# p.parcel_id = 'ldhgkjhdf'
# p.recipient_name = 'ejhguergherugh'
# p.gggg = 'kjkjjkj'

print(p.__dict__)