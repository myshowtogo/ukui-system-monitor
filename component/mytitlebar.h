/*
 * Copyright (C) 2020 KylinSoft Co., Ltd.
 *
 * Authors:
 *  Kobe Lee    xiangli@ubuntukylin.com/kobe24_lixiang@126.com
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef MYTITLEBAR_H
#define MYTITLEBAR_H

#include <QFrame>

class QHBoxLayout;
class MyTristateButton;

class MyTitleBar : public QFrame
{
    Q_OBJECT
public:
    MyTitleBar(const QString &title = "", bool needMin = false, QWidget *parent = 0);
    ~MyTitleBar();

    void setLeftContent(QWidget *content);
    void setMiddleContent(QWidget *content);

    void initLeftContent();
    void initMiddleContent();
    void initRightContent();
    void initWidgets();

signals:
    void minSignal();
    void closeSignal();

private:
    QString m_title;
    bool m_needMin;
    QHBoxLayout *m_layout = nullptr;
    QHBoxLayout *m_lLayout = nullptr;
    QHBoxLayout *m_mLayout = nullptr;
    QHBoxLayout *m_rLayout = nullptr;
};

#endif // MYTITLEBAR_H
