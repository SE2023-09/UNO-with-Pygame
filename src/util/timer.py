from datetime import datetime, timedelta
from typing import Optional


class Timer:
    # Timer 클래스 생성자
    def __new__(cls, *args, **kwargs):
        return super(Timer, cls).__new__(cls)

    # Timer 객체 초기화 메서드
    def __init__(self) -> None:
        self.__timestarted: Optional[datetime] = None
        self.__timepaused: Optional[datetime] = None
        self.__paused: bool = False

    # 타이머 시작 메서드
    def start(self) -> None:
        self.__timestarted = datetime.now()
        return None

    # 타이머 일시정지 메서드
    def pause(self) -> None:
        if self.__timestarted is None:
            raise ValueError("Timer not started")
        if self.__paused:
            raise ValueError("Timer is already paused")
        self.__timepaused = datetime.now()
        self.__paused = True
        return None

    # 타이머 재개 메서드
    def resume(self) -> None:
        if self.__timestarted is None:
            raise ValueError("Timer not started")
        if not self.__paused:
            raise ValueError("Timer is not paused")
        pausetime = datetime.now() - self.__timepaused
        self.__timestarted += pausetime
        self.__timepaused = None
        self.__paused = False
        return None

    # 타이머의 현재 시간을 반환하는 메서드
    def get(self) -> timedelta:
        if self.__timestarted is None:
            raise ValueError("Timer not started")
        if self.__paused:
            return self.__timepaused - self.__timestarted
        else:
            return datetime.now() - self.__timestarted

    # 타이머 정지(초기화) 메서드
    def stop(self) -> None:
        self.__timestarted = None
        self.__timepaused = None
        self.__paused = False
        return None

    # 타이머 상태 조회 메서드
    def status(self) -> str:
        status: Optional[str] = None
        if self.__paused is True:
            status = "paused"
            pass
        elif self.__timestarted is None and self.__timepaused is None:
            status = "stopped"
            pass
        elif self.__timestarted is not None and self.__timepaused is None:
            status = "running"
            pass

        return status
