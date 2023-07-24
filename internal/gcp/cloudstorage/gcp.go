package cloudstorage

import (
	"context"
    cloudtasks "google.golang.org/api/cloudtasks/v2"
)

func CreateCloudTaskQueue(ctx context.Context, projectID, locationID string, queue *cloudtasks.Queue) (*cloudtasks.Queue, error) {
    service, err := cloudtasks.NewService(ctx)
    if err != nil {
        return nil, err
    }

    parent := "projects/" + projectID + "/locations/" + locationID
    queue, err = service.Projects.Locations.Queues.Create(parent, queue).Do()
    if err != nil {
        return nil, err
    }

    return queue, nil
}

func UpdateCloudTaskQueue(ctx context.Context, projectID, locationID, queueID string, queue *cloudtasks.Queue) (*cloudtasks.Queue, error) {
    service, err := cloudtasks.NewService(ctx)
    if err != nil {
        return nil, err
    }

    name := "projects/" + projectID + "/locations/" + locationID + "/queues/" + queueID
    queue, err = service.Projects.Locations.Queues.Patch(name, queue).Do()
    if err != nil {
        return nil, err
    }

    return queue, nil
}