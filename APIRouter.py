from fastapi import APIRouter
from controllers.userController import router as userRouter
#from controllers.vehicleController import router as vehicleRouter
#from controllers.routeController import router as routeController

apiRouter = APIRouter(prefix="/api/v1")

apiRouter.include_router(userRouter)
#apiRouter.include_router(vehicleRouter)
#apiRouter.include_router(routeController)