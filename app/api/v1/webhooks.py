from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.models.webhook import WebhookDelivery, WebhookSubscription
from app.schemas.webhook import WebhookDeliveryOut, WebhookSubscriptionCreate, WebhookSubscriptionOut

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.get("/subscriptions", response_model=list[WebhookSubscriptionOut])
async def list_subscriptions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebhookSubscription))
    return result.scalars().all()


@router.post(
    "/subscriptions", response_model=WebhookSubscriptionOut, status_code=status.HTTP_201_CREATED
)
async def create_subscription(payload: WebhookSubscriptionCreate, db: AsyncSession = Depends(get_db)):
    subscription = WebhookSubscription(**payload.model_dump())
    db.add(subscription)
    await db.commit()
    await db.refresh(subscription)
    return subscription


@router.get("/deliveries", response_model=list[WebhookDeliveryOut])
async def list_deliveries(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebhookDelivery).order_by(WebhookDelivery.id.desc()).limit(50))
    return result.scalars().all()


@router.get("/subscriptions/{subscription_id}", response_model=WebhookSubscriptionOut)
async def get_subscription(subscription_id: int, db: AsyncSession = Depends(get_db)):
    subscription = await db.get(WebhookSubscription, subscription_id)
    if subscription is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subscription not found")
    return subscription
