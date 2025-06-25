from datetime import datetime
from app.models import Listing, Host, Address, Review, Location


location = Location(
    type="Point",
    coordinates=[123, 456],
    is_location_exact=True,
)

address = Address(
    street="123 Main St",
    government_area="Test Government Area",
    market="Test Market",
    country="Test Country",
    country_code="US",
    location=location,
)

def test_address_model():
    assert address.street == "123 Main St"
    assert address.government_area == "Test Government Area"
    assert address.market == "Test Market"
    assert address.country == "Test Country"
    assert address.country_code == "US"
    assert address.location.type == "Point"
    assert address.location.coordinates == [123, 456]

host = Host(
    host_id="123",
    host_url="https://www.airbnb.com/users/123",
    host_name="Test Host",
    host_location="Test Host Location",
    host_about="Test Host About",
    host_thumbnail_url="https://www.airbnb.com/users/123/thumbnail",
    host_picture_url="https://www.airbnb.com/users/123/picture",
    host_is_superhost=True,
    host_has_profile_pic=True,
    host_identity_verified=True,
)

def test_host_model():
    assert host.host_id == "123"
    assert host.host_url == "https://www.airbnb.com/users/123"
    assert host.host_name == "Test Host"
    assert host.host_location == "Test Host Location"
    assert host.host_about == "Test Host About"
    assert host.host_thumbnail_url == "https://www.airbnb.com/users/123/thumbnail"
    assert host.host_picture_url == "https://www.airbnb.com/users/123/picture"
    assert host.host_is_superhost == True
    assert host.host_has_profile_pic == True
    assert host.host_identity_verified == True

review = Review(
    listing_id="123",
    reviewer_id="123",
)

def test_review_model():
    assert review.listing_id == "123"
    assert review.reviewer_id == "123"


listing = Listing(
    listing_url="https://www.airbnb.com/listings/123",
    name="Test Listing",
    summary="Test Summary",
    space="Test Space",
    description="Test Description",
    access="Test Access",
    house_rules="Test House Rules",
    property_type="Test Property Type",
    room_type="Test Room Type",
    bed_type="Test Bed Type",
    minimum_nights=1,
    maximum_nights=30,
    cancellation_policy="Test Cancellation Policy",
    accommodates=4,
    bedrooms=2,
    beds=3,
    number_of_reviews=10,
    amenities=["Test Amenity 1", "Test Amenity 2"],
    price=100,
    extra_people=10,
    guests_included=2,
    images={},
    host=host,
    address=address,
    availability={},
    review_scores={},
    reviews=[review],
    text_embeddings=[1.0, 2.0, 3.0],
)

def test_listing_model():
    assert listing.listing_url == "https://www.airbnb.com/listings/123"
    assert listing.name == "Test Listing"
    assert listing.summary == "Test Summary"
    assert listing.space == "Test Space"
    assert listing.description == "Test Description"
    assert listing.access == "Test Access"
    assert listing.house_rules == "Test House Rules"
    assert listing.property_type == "Test Property Type"
    assert listing.room_type == "Test Room Type"
    assert listing.bed_type == "Test Bed Type"
    assert listing.minimum_nights == 1
    assert listing.maximum_nights == 30
    assert listing.cancellation_policy == "Test Cancellation Policy"
    assert listing.accommodates == 4
    assert listing.bedrooms == 2
    assert listing.beds == 3
    assert listing.number_of_reviews == 10
    assert listing.amenities == ["Test Amenity 1", "Test Amenity 2"]
    assert listing.price == 100
    assert listing.extra_people == 10
    assert listing.guests_included == 2
    assert listing.images == {}
    assert listing.host == host
    assert listing.address == address
    assert listing.availability == {}
    assert listing.review_scores == {}
    assert listing.reviews == [review]
    assert listing.text_embeddings == [1.0, 2.0, 3.0]

